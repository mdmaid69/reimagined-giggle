  import os
  def delete_file(file_name):
        os.remove(file_name)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)