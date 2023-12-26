def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)