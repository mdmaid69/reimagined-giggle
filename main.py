  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
n = 10
print("Powers of 2:", [2**x for x in range(n)])