  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)