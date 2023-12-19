import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)