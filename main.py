import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)