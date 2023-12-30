  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)