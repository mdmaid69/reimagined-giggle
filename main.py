  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import os
def get_file_size(filename):
        return os.path.getsize(filename)