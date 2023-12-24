def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)