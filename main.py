  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()