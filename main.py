  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()