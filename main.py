  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)