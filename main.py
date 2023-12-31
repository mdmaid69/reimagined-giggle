  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
n = 10
print("Square numbers:", [x**2 for x in range(n)])