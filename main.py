import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino