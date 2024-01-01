import http.server
def start_http_server(port):
        http.server.HTTPServer(("", port), http.server.SimpleHTTPRequestHandler).serve_forever()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"