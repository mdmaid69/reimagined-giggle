import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)