  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
text = "Hello, world!"
print("Reversed:", text[::-1])