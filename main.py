def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)