  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import datetime
def get_current_date():
        return datetime.date.today()