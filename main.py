  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)