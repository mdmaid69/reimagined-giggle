  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import shutil
def delete_directory(path):
        shutil.rmtree(path)