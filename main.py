  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)