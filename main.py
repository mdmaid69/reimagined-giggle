import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()