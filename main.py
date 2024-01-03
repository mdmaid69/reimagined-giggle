text = "Hello, world!"
print("Characters:", len(text))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)