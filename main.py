  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)