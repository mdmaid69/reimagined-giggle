import os
def remove_directory(path):
        os.rmdir(path)
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino