  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)