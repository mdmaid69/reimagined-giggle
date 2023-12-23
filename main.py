  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
x = 10
y = 20
print("Sum:", x + y)