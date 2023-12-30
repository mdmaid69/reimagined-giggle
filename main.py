  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper