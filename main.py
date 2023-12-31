import array
def iterate_over_array(array):
        for item in array:
        print(item)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()