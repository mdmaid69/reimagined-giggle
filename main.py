  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import os
def list_files_in_directory(path):
        return os.listdir(path)