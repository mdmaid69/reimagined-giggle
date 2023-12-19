  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)