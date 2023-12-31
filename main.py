  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import os
def change_working_directory(path):
        os.chdir(path)