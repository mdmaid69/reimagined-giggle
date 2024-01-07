  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import os
def list_files_in_directory(path):
        return os.listdir(path)