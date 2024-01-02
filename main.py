  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)