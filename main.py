import datetime
def get_current_date():
        return datetime.date.today()
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)