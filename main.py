import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)