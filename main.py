  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)