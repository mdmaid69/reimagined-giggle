  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize