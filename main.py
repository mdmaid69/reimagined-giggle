  import os
  def get_base_name(path):
        return os.path.basename(path)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)