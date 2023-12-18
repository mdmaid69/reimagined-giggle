  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)