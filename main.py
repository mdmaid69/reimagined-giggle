  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue