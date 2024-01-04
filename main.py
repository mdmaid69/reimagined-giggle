n = 10
print("Cube numbers:", [x**3 for x in range(n)])
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns