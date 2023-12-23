  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import os
def list_files_in_directory(path):
        return os.listdir(path)