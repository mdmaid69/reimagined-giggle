text = "Hello, world!"
print("Reversed:", text[::-1])
  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode