import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)