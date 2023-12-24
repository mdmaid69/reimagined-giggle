import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()