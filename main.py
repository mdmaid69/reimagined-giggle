text = "Hello, world!"
print("Characters:", len(text))
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size