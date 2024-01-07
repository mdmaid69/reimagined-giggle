  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)