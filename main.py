  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
x = 10
y = 20
print("Sum:", x + y)