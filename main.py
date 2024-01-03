  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)