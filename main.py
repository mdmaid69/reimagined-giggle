  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import os
def remove_directory(path):
        os.rmdir(path)