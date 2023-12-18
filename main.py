def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)