  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import os
def remove_directory(path):
        os.rmdir(path)