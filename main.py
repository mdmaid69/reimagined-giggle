  import os
  def get_base_name(path):
        return os.path.basename(path)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)