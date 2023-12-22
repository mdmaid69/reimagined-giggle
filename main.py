import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)