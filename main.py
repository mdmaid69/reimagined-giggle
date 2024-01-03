text = "Hello, world!"
print("Words:", len(text.split()))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)