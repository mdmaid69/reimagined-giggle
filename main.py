  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()