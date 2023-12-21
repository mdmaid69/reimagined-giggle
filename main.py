import sklearn.datasets
print(sklearn.datasets.load_iris())
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()