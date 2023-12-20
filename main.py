import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()