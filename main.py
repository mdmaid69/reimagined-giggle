  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))