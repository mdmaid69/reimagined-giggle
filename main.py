  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def is_palindrome(s):
        return s == s[::-1]