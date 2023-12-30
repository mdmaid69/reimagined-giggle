  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import shutil
def delete_directory(path):
        shutil.rmtree(path)