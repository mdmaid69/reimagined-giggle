  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)