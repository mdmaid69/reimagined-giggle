n = 10
print("Powers of 2:", [2**x for x in range(n)])
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns