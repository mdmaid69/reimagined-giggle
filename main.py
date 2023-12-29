def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)