  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
text = "Hello, world!"
print("Reversed:", text[::-1])