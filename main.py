def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)