  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b