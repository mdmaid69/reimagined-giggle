  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b