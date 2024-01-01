import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)