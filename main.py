  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b