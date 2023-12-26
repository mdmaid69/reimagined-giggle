  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))