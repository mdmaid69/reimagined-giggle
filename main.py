sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()