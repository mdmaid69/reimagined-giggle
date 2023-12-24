def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)