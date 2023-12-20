  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])