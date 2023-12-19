import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)