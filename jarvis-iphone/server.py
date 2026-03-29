#!/usr/bin/env python3
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from urllib.error import HTTPError, URLError
import re

HOST = os.getenv("JARVIS_HOST", "0.0.0.0")
PORT = int(os.getenv("JARVIS_PORT", "8787"))
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
MODEL = os.getenv("JARVIS_MODEL", "openrouter/auto")
SYSTEM_PROMPT = os.getenv(
    "JARVIS_SYSTEM_PROMPT",
    "Ты голосовой ассистент Джарвис. Отвечай кратко, дружелюбно и по делу."
)

CONTEXT_FILES = [
    "/root/.openclaw/workspace/USER.md",
    "/root/.openclaw/workspace/MEMORY.md",
]


def load_project_context(max_chars: int = 12000) -> str:
    chunks = []
    for path in CONTEXT_FILES:
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            chunks.append(f"\n\n# Context from {os.path.basename(path)}\n{text}")
        except Exception:
            continue
    merged = "".join(chunks).strip()
    if len(merged) > max_chars:
        merged = merged[:max_chars]
    return merged


def search_web_duckduckgo(query: str, limit: int = 5) -> str:
    q = (query or "").strip()
    if not q:
        return "Пустой запрос для интернет-поиска."

    url = f"https://duckduckgo.com/html/?q={quote_plus(q)}"
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36"
        },
    )

    try:
        with urlopen(req, timeout=20) as resp:
            html = resp.read().decode("utf-8", errors="ignore")

        items = []
        pattern = re.compile(
            r'<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
            re.IGNORECASE | re.DOTALL,
        )
        for m in pattern.finditer(html):
            href = m.group(1)
            title = re.sub(r"<.*?>", "", m.group(2))
            title = re.sub(r"\s+", " ", title).strip()
            if not title:
                continue
            items.append((title, href))
            if len(items) >= limit:
                break

        if not items:
            return "Не нашёл результатов в интернете по этому запросу."

        lines = ["Нашёл в интернете:"]
        for i, (title, href) in enumerate(items, 1):
            lines.append(f"{i}. {title} — {href}")
        return "\n".join(lines)
    except Exception as e:
        return f"Ошибка интернет-поиска: {e}"


def ask_llm(user_text: str) -> str:
    if not OPENROUTER_API_KEY:
        return "Нужен API ключ OPENROUTER_API_KEY на сервере."

    lower = user_text.lower().strip()
    web_prefixes = [
        "найди в интернете",
        "поиск в интернете",
        "найди в сети",
        "поищи в интернете",
    ]
    for p in web_prefixes:
        if lower.startswith(p):
            q = user_text[len(p):].strip(" :,-")
            return search_web_duckduckgo(q or user_text)

    project_context = load_project_context()

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if project_context:
        messages.append(
            {
                "role": "system",
                "content": "Контекст пользователя и проектов (используй для персонализации, но не цитируй дословно приватные данные):\n" + project_context,
            }
        )
    messages.append({"role": "user", "content": user_text})

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.5,
        "max_tokens": 220,
    }

    req = Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://jarvis.local",
            "X-Title": "Jarvis iPhone Shortcut",
        },
        method="POST",
    )

    try:
        with urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            msg = (data.get("choices") or [{}])[0].get("message") or {}
            content = msg.get("content")

            if isinstance(content, str) and content.strip():
                return content.strip()

            if isinstance(content, list):
                parts = []
                for item in content:
                    if isinstance(item, dict) and isinstance(item.get("text"), str):
                        parts.append(item["text"])
                merged = "\n".join([p for p in parts if p.strip()]).strip()
                if merged:
                    return merged

            refusal = msg.get("refusal")
            if isinstance(refusal, str) and refusal.strip():
                return refusal.strip()

            return "Не удалось получить текстовый ответ от модели. Попробуй ещё раз."
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        return f"Ошибка LLM HTTP {e.code}: {body[:400]}"
    except URLError as e:
        return f"Ошибка сети: {e}"
    except Exception as e:
        return f"Внутренняя ошибка: {e}"


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, code: int, obj: dict):
        out = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

    def do_GET(self):
        if self.path == "/health":
            self._send_json(200, {"ok": True, "service": "jarvis"})
        else:
            self._send_json(404, {"ok": False, "error": "not found"})

    def do_POST(self):
        if self.path != "/jarvis":
            self._send_json(404, {"ok": False, "error": "not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length > 0 else b"{}"
            body = json.loads(raw.decode("utf-8"))
            user_text = (body.get("text") or "").strip()
            if not user_text:
                self._send_json(400, {"ok": False, "error": "field 'text' is required"})
                return

            answer = ask_llm(user_text)
            self._send_json(200, {"ok": True, "reply": answer})
        except json.JSONDecodeError:
            self._send_json(400, {"ok": False, "error": "invalid JSON"})
        except Exception as e:
            self._send_json(500, {"ok": False, "error": str(e)})

    def log_message(self, format, *args):
        # quieter logs
        return


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Jarvis server started on http://{HOST}:{PORT}")
    server.serve_forever()
