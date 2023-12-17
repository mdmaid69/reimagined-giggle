  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)