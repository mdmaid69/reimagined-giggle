  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
i = 0
while i < 5:
        print(i)
        i += 1