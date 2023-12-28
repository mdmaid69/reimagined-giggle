  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)