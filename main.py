import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev