  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import os
def list_files_in_directory(path):
        return os.listdir(path)