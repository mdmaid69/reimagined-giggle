  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)