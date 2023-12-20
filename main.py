  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import datetime
def get_today_date():
        return datetime.date.today()