  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper