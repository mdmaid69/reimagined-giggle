  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)