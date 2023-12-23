  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import os
def get_file_size(filename):
        return os.path.getsize(filename)