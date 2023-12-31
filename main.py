  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)