  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets