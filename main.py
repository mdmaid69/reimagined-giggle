n = 10
print("Powers of 2:", [2**x for x in range(n)])
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)