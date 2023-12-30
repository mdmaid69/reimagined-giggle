  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)