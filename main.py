  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))