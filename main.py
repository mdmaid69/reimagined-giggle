  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b