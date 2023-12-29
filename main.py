  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare