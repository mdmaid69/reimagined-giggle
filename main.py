  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b