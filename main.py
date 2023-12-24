  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b