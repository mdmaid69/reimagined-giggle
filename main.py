  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
n = 10
print("Powers of 2:", [2**x for x in range(n)])