  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)