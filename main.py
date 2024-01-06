  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import datetime
def get_today_date():
        return datetime.date.today()