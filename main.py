import sys
def add_to_python_path(path):
        sys.path.append(path)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)