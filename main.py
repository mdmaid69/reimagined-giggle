  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b