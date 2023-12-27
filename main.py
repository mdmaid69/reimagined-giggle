import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)