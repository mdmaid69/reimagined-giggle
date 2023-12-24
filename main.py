  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))