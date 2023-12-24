import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)