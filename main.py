import os
def remove_directory(path):
        os.rmdir(path)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)