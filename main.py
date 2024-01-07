  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
n = 10
print("Square numbers:", [x**2 for x in range(n)])