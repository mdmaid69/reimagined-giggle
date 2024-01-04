  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)