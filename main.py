  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]