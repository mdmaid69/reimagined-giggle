def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)