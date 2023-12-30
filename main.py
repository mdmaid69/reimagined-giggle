  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()