  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True