import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))