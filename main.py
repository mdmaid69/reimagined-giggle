  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
for i in range(10): print(i)