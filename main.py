  import os
  def split_path(path):
        return os.path.split(path)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize