  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)