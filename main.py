text = "Hello, world!"
print("Characters:", len(text))
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino