n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)