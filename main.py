def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)