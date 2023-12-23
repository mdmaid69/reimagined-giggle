import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"