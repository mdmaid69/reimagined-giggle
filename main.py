  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)