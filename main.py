  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import shutil
def delete_directory(path):
        shutil.rmtree(path)