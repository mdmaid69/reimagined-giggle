text = "Hello, world!"
print("Words:", len(text.split()))
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)