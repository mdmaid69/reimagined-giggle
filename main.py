  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
n = 10
print("Cube numbers:", [x**3 for x in range(n)])