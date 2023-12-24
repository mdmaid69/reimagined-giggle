import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)