  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
i = 0
while i < 5:
        print(i)
        i += 1