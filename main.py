  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)