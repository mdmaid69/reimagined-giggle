import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()