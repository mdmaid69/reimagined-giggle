from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)