  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)