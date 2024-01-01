import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)