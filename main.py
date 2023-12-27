def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)