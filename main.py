def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)