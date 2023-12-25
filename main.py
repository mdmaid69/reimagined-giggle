  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)