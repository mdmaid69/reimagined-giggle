import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)