def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)