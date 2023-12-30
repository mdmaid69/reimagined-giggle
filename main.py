  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)