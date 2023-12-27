import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()