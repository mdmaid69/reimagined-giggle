  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)