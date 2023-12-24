  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import os
def remove_directory(path):
        os.rmdir(path)