  import os
  def get_base_name(path):
        return os.path.basename(path)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)