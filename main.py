  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)