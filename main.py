  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
n = 10
print("Powers of 2:", [2**x for x in range(n)])