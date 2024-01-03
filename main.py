  import os
  def split_path(path):
        return os.path.split(path)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)