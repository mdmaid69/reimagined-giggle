  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
text = "Hello, world!"
print("Reversed:", text[::-1])