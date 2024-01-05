  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))