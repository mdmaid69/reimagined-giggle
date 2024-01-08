n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)