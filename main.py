  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import os
  def delete_file(file_name):
        os.remove(file_name)