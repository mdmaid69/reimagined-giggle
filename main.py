  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)