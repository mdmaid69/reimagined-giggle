import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)