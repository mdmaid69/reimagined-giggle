  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"