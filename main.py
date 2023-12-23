  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import os
def change_working_directory(path):
        os.chdir(path)