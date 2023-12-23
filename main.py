  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
x = 10
y = 20
print("Sum:", x + y)