  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import datetime
def get_current_date():
        return datetime.date.today()