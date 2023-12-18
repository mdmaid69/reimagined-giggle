  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))