text = "Hello, world!"
print("Words:", len(text.split()))
  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev