import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)