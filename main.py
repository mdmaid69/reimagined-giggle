  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)