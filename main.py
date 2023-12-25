  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)