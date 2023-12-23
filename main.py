import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev