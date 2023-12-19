  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
name = "Python"
print("Hello,", name)