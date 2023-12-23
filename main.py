  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)