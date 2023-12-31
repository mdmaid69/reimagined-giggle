  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
i = 0
while i < 5:
        print(i)
        i += 1