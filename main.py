  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import os
def get_file_size(filename):
        return os.path.getsize(filename)