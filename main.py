  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
text = "Hello, world!"
print("Reversed:", text[::-1])