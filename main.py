  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
text = "Hello, world!"
print("Characters:", len(text))