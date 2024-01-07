  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import os
def get_file_size(filename):
        return os.path.getsize(filename)