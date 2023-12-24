  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import os
def get_current_working_directory():
        return os.getcwd()