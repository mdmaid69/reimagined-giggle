import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()