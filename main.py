  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)