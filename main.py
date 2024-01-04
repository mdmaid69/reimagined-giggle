  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
n = 10
print("Square numbers:", [x**2 for x in range(n)])