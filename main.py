text = "Hello, world!"
print("Words:", len(text.split()))
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)