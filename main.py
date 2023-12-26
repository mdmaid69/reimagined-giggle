  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()