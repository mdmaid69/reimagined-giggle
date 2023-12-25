  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)