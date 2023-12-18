  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])