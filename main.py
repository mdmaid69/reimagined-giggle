  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import datetime
def get_today_date():
        return datetime.date.today()