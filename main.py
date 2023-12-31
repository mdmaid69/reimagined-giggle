  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
n = 10
print("Powers of 2:", [2**x for x in range(n)])