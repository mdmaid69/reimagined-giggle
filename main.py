  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)