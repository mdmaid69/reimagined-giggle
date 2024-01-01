  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import shutil
def delete_directory(path):
        shutil.rmtree(path)