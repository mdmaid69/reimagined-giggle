def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)