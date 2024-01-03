  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import os
def remove_directory(path):
        os.rmdir(path)