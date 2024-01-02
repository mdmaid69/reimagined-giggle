import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks