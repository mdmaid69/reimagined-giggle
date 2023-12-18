  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))