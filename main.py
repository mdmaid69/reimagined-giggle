  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  import os
  def delete_file(file_name):
        os.remove(file_name)