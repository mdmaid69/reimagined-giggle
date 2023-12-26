text = "Hello, world!"
print("Characters:", len(text))
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink