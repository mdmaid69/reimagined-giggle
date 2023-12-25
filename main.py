n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)