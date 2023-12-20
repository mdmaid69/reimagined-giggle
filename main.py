def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)