  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))