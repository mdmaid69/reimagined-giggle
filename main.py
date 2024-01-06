  import os
  def get_current_directory():
        return os.getcwd()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)