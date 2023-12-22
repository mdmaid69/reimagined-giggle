  import os
  def get_current_directory():
        return os.getcwd()
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b