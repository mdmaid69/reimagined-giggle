import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)