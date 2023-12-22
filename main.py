  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
x = 10
y = 20
print("Sum:", x + y)