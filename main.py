  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import datetime
def get_today_date():
        return datetime.date.today()