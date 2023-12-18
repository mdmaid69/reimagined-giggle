import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)