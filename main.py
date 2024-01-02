  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b