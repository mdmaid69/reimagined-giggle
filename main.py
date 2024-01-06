  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
name = "Python"
print("Hello,", name)