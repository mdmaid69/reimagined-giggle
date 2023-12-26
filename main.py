  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import os
  def delete_file(file_name):
        os.remove(file_name)