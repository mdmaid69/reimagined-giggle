import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)