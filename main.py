  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import os
def list_files_in_directory(path):
        return os.listdir(path)