  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))