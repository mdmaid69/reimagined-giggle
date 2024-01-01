  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)