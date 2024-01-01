  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import os
def list_files_in_directory(path):
        return os.listdir(path)