  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)