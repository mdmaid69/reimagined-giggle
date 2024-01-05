  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
n = 10
print("Powers of 2:", [2**x for x in range(n)])