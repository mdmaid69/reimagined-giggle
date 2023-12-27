  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)