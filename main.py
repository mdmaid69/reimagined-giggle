  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))