  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))