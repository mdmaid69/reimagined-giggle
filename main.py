import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)