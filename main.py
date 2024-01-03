  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
text = "Hello, world!"
print("Reversed:", text[::-1])