  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)