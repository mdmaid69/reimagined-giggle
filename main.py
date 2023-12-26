  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)