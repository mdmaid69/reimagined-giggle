import datetime
def get_today_date():
        return datetime.date.today()
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino