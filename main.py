  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)