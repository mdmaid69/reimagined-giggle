  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
text = "Hello, world!"
print("Reversed:", text[::-1])