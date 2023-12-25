  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))