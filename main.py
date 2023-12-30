  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import datetime
def get_today_date():
        return datetime.date.today()