  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import os
def remove_directory(path):
        os.rmdir(path)