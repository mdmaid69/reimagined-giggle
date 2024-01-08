import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)