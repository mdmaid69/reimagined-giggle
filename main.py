  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)