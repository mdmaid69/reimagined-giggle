  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b