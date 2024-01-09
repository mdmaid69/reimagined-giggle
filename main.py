  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import os
def get_current_working_directory():
        return os.getcwd()