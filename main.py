  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)