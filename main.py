import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]