  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)