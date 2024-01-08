  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)