  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import os
def list_files_in_directory(path):
        return os.listdir(path)