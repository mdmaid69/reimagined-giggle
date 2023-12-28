  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags