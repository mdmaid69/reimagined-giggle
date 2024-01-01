  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))