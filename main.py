  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)