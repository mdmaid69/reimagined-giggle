  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()