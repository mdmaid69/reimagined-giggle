  import os
  def get_current_working_directory():
        return os.getcwd()
import os
def change_working_directory(path):
        os.chdir(path)