  import os
  def get_base_name(path):
        return os.path.basename(path)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b