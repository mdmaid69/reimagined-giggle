  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)