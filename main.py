  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
n = 10
print("Square numbers:", [x**2 for x in range(n)])