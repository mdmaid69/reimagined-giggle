  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)