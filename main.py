  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)