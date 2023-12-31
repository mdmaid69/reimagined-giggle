  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)