  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)