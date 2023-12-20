  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper