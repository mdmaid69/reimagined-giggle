  import os
  def get_current_working_directory():
        return os.getcwd()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)