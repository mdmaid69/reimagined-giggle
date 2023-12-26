  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
n = 10
print("Powers of 2:", [2**x for x in range(n)])