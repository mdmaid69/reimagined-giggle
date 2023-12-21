  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import os
def remove_directory(path):
        os.rmdir(path)