import datetime
def get_today_date():
        return datetime.date.today()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)