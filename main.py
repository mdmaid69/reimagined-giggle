  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)