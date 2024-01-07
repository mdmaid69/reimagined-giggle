  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))