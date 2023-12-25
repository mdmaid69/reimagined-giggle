  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)