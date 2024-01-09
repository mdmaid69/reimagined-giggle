  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
text = "Hello, world!"
print("Uppercase:", text.upper())