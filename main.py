  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize