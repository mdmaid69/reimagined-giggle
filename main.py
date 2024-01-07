  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
x = 10
y = 20
print("Sum:", x + y)