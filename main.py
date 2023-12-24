  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)