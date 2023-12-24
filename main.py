import platform
def get_python_version():
        return platform.python_version()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)