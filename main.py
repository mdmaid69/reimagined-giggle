  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)