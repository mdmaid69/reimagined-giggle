  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])