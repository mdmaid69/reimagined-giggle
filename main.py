  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
for i in range(10): print(i)