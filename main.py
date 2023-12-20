import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)