  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import glob
def find_files(pattern):
        return glob.glob(pattern)