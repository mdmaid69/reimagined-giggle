  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)