n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def delete_file(file_name):
        os.remove(file_name)