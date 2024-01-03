import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)