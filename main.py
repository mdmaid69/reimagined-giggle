import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)