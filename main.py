import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()