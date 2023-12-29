  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)