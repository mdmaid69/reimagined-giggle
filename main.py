  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)