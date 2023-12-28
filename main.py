  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b