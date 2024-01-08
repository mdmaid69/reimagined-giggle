  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)