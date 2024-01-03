  import os
  def delete_file(file_name):
        os.remove(file_name)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)