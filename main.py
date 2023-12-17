  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)