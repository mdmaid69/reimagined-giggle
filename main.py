  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])