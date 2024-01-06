def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)