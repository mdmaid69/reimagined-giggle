  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)