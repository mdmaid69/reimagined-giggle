  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
n = 10
print("Square numbers:", [x**2 for x in range(n)])