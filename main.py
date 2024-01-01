import os
def change_working_directory(path):
        os.chdir(path)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()