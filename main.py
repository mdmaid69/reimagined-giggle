  import os
  def delete_file(file_name):
        os.remove(file_name)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)