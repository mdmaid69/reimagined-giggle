import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)