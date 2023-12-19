  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
text = "Hello, world!"
print("Characters:", len(text))