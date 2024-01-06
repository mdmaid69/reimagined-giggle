  import os
  def get_directory_name(path):
        return os.path.dirname(path)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b