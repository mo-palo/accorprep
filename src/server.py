from http.server import HTTPServer, BaseHTTPRequestHandler
import json, os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'checklist-data.json')

class Handler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path != '/data':
            self.send_error(404); return
        self._cors()
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'rb') as f:
                data = f.read()
        else:
            data = b'{}'
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path != '/data':
            self.send_error(404); return
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length)
        json.loads(body)  # validate JSON — raises 500 on bad input
        with open(DATA_FILE, 'wb') as f:
            f.write(body)
        self._cors()
        self.end_headers()

    def _cors(self):
        self.send_response(200)
        # Reflect Origin so both file:// (null) and http://localhost work
        origin = self.headers.get('Origin', '*')
        self.send_header('Access-Control-Allow-Origin', origin)
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def log_message(self, *args): pass

print('Data server running at http://localhost:7823  (Ctrl+C to stop)')
HTTPServer(('localhost', 7823), Handler).serve_forever()
