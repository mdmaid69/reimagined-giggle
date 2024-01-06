import json
def read_from_json(json_string):
        return json.loads(json_string)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)