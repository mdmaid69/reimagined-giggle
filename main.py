  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))