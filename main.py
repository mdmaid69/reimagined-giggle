  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import os
  def get_base_name(path):
        return os.path.basename(path)