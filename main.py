  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))