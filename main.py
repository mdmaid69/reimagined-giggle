  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import datetime
def get_today_date():
        return datetime.date.today()