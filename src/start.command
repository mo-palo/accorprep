#!/bin/bash
# Accor AI PDLC — Data Server Launcher
# Double-click this file in Finder to start the server and open the app.

cd "$(dirname "$0")"

# Open the app in the default browser first
open index.html

# Start the server (keep this window open — close it to stop the server)
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Accor AI PDLC — Data Server"
echo "  http://localhost:7823"
echo "  Close this window to stop."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
python3 server.py
