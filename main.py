  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))