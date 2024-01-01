  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)