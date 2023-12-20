import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize