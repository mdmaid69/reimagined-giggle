  import os
  def get_current_directory():
        return os.getcwd()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)