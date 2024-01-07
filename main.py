  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)