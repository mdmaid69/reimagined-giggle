import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)