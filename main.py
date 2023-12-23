  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import platform
def get_os_info():
        return platform.uname()