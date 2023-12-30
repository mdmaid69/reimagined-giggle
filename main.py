  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
text = "Hello, world!"
print("Words:", len(text.split()))