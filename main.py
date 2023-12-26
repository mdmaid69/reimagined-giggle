  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
x = 10
y = 20
print("Sum:", x + y)