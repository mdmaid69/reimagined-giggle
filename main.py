  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b