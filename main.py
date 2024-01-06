import os
def remove_directory(path):
        os.rmdir(path)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize