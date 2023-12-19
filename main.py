  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b