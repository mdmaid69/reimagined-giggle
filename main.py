def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)