  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)