  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)