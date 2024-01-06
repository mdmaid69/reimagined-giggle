  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)