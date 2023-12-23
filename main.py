  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days