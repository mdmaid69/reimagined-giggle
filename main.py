  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))