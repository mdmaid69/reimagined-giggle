def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)