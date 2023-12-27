  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b