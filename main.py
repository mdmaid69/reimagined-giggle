  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)