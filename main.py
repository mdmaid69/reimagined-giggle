def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()