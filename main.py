import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)