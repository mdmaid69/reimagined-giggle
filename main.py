text = "Hello, world!"
print("Uppercase:", text.upper())
  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime