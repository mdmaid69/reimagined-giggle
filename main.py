import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)