  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)