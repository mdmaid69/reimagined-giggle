  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
  import os
  def delete_file(file_name):
        os.remove(file_name)