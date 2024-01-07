import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)