  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))