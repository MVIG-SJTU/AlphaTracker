import sys
import socketserver
import webbrowser
from http.server import SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable Cross-Origin Resource Sharing (CORS)
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


if sys.version_info < (3, 7, 5):
    # Fix for WASM MIME type for older Python versions
    Handler.extensions_map[".wasm"] = "application/wasm"


if __name__ == "__main__":
    port = 8000
    with socketserver.TCPServer(("", port), Handler, False) as httpd:
        httpd.allow_reuse_address = True
        httpd.server_bind()
        httpd.server_activate()
        print("Serving at: http://127.0.0.1:{}".format(port))
        webbrowser.open_new("http://127.0.0.1:{}".format(port))
        httpd.serve_forever()
