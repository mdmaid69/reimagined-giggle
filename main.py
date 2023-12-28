  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)