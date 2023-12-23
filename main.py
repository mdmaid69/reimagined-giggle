  import os
  def get_current_directory():
        return os.getcwd()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)