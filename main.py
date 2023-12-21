  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days