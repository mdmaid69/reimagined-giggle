import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)