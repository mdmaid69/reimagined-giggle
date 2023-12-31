import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)