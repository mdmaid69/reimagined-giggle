def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]