import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"