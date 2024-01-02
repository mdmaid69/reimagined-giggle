  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)