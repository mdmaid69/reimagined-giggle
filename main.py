import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)