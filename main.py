def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)