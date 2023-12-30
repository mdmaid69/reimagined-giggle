import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
def count_characters(sentence):
        return len(sentence)