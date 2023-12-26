import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list