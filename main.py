  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)