import os
def remove_directory(path):
        os.rmdir(path)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)