n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]