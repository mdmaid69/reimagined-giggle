  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import os
def change_working_directory(path):
        os.chdir(path)