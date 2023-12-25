  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))