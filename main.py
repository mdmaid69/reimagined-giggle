  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import os
def get_file_size(filename):
        return os.path.getsize(filename)