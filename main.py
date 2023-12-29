  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)