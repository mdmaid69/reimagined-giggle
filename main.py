def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)