  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
x = 10
y = 20
print("Sum:", x + y)