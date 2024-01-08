  import os
  def split_path(path):
        return os.path.split(path)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b