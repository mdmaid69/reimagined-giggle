  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
x = 10
y = 20
print("Sum:", x + y)