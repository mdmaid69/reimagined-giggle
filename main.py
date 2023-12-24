  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size