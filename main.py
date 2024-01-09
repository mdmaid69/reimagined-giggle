def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)