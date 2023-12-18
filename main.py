import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)