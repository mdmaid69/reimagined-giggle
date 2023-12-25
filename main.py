  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)