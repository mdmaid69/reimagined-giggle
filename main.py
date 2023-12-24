  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
n = 10
print("Cube numbers:", [x**3 for x in range(n)])