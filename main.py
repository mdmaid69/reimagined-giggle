import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)