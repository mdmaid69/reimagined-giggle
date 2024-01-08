import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)