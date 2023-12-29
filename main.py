  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
x = 10
y = 20
print("Sum:", x + y)