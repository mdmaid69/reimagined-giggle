import json
def read_from_json(json_string):
        return json.loads(json_string)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)