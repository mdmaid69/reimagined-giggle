  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
n = 10
print("Square numbers:", [x**2 for x in range(n)])