import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)