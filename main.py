  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
n = 10
print("Square numbers:", [x**2 for x in range(n)])