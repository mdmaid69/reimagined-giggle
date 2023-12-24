import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)