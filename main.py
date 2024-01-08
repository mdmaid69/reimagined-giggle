  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
text = "Hello, world!"
print("Reversed:", text[::-1])