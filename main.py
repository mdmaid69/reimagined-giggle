  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))