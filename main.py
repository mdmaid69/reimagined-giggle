  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)