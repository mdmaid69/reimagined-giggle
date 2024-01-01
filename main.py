  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import datetime
def get_current_date():
        return datetime.date.today()