  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)