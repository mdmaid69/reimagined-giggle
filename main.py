  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)