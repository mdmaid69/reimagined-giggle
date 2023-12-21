  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
n = 10
print("Powers of 2:", [2**x for x in range(n)])