  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b