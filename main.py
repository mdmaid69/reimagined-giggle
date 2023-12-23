  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import os
def remove_directory(path):
        os.rmdir(path)