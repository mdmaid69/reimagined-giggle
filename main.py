  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
n = 10
print("Square numbers:", [x**2 for x in range(n)])