import os
def get_environment_variable(var):
        return os.getenv(var)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)