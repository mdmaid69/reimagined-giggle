  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import datetime
def get_today_date():
        return datetime.date.today()