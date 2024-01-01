  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a