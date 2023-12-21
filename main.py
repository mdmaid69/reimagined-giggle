import os
def change_working_directory(path):
        os.chdir(path)
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks