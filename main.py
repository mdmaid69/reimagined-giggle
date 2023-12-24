def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)