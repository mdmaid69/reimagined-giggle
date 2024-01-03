  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time