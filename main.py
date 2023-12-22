  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
x = 10
y = 20
print("Sum:", x + y)