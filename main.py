  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)