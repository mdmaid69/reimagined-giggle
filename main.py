  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
x = 10
y = 20
print("Sum:", x + y)