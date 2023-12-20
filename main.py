import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])