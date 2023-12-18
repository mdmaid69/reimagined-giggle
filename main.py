import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)