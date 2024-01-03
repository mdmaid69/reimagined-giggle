import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)