  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import os
def remove_directory(path):
        os.rmdir(path)