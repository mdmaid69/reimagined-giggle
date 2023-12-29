  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
x = 10
y = 20
print("Sum:", x + y)