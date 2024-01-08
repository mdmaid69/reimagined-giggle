  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)