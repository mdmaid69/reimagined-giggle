  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
n = 10
print("Cube numbers:", [x**3 for x in range(n)])