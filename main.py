  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)