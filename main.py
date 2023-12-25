  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  import os
  def get_current_working_directory():
        return os.getcwd()