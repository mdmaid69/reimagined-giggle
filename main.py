def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import os
  def split_path(path):
        return os.path.split(path)