# TOOLS.md - What You Can Really Do

## Real Scripts on This Server

### Voice Messages: /root/speak.py
Sends a voice message to Telegram.
Usage: python3 /root/speak.py "your text here" "chat_id"
Example: python3 /root/speak.py "Searching for products" "6566313188"
RULE: After EVERY text response, call this script to send a voice version.

### 1688 Search: /root/search_1688.py
Real search on 1688.com using Playwright browser.
Usage: python3 /root/search_1688.py "search keyword in Chinese"
Example: python3 /root/search_1688.py
RULE: ALWAYS use this script for 1688 searches. NEVER invent product links.

## What You Can Do (Real)
- Execute bash commands on Ubuntu 24.04 server
- Read/write files in /root/.openclaw/workspace/
- Send voice messages via speak.py
- Search 1688.com via search_1688.py
- Install packages with apt-get and pip3 --break-system-packages

## What You CANNOT Do (Be Honest)
- Send voice without speak.py script
- Search 1688 without search_1688.py script
- Take screenshots without explicitly using playwright
- Access external services directly (only via scripts)

## Server Info
- OS: Ubuntu 24.04
- IP: 155.212.225.175
- Workspace: /root/.openclaw/workspace/
- Bot Token: stored in /root/.openclaw/openclaw.json
- User Chat ID: 6566313188
