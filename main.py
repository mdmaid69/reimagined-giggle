  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days