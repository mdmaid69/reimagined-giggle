  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import os
def list_files_in_directory(path):
        return os.listdir(path)