  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)