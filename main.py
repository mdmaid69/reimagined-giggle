def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)