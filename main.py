import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)