import os
def remove_directory(path):
        os.rmdir(path)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)