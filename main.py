  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import os
def get_current_working_directory():
        return os.getcwd()