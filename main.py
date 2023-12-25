  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b