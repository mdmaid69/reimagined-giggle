  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))