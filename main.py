  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
text = "Hello, world!"
print("Reversed:", text[::-1])