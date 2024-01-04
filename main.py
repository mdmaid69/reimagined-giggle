import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)