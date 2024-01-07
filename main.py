import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))