import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import os
  def get_current_directory():
        return os.getcwd()