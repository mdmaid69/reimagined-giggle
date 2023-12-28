  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import os
def get_current_working_directory():
        return os.getcwd()