  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])