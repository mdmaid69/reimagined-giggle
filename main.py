import os
def remove_directory(path):
        os.rmdir(path)
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime