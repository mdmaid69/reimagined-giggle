  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))