  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
n = 10
print("Powers of 2:", [2**x for x in range(n)])