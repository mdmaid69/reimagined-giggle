  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b