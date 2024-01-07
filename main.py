  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare