def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)