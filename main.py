  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks