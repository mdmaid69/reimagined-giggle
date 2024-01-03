  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))