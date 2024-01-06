def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)