def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)