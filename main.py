  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
text = "Hello, world!"
print("Characters:", len(text))