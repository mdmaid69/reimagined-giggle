import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()