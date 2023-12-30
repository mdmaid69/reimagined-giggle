  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])