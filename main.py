  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)