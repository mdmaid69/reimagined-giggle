  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)