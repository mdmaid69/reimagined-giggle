n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)