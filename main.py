  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)