  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
n = 10
print("Powers of 2:", [2**x for x in range(n)])