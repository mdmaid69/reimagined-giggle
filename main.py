  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)