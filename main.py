  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"