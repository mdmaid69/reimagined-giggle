  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)