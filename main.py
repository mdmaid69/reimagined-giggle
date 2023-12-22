  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)