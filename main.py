  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import itertools
print(list(itertools.permutations([1, 2, 3])))