  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import os
def list_files_in_directory(path):
        return os.listdir(path)