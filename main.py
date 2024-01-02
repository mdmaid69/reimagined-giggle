import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)