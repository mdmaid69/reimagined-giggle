  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"