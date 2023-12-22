from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)