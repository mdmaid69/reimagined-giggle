  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)