  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import os
def change_working_directory(path):
        os.chdir(path)