import datetime
def get_today_date():
        return datetime.date.today()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)