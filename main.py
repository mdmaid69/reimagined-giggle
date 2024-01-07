import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)