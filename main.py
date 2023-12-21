  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)