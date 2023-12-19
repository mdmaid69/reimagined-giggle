  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))