  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import os
def get_file_size(filename):
        return os.path.getsize(filename)