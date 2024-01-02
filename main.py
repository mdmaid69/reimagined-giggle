  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a