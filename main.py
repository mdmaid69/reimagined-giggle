  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))