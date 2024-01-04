  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)