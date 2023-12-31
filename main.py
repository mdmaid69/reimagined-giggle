  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev