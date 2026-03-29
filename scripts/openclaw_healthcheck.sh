#!/usr/bin/env bash
set -euo pipefail

echo "=== OPENCLAW STATUS ==="
openclaw status || true

echo
echo "=== GATEWAY STATUS ==="
openclaw gateway status || true
