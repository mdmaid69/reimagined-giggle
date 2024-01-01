  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b