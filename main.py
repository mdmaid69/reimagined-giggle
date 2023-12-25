  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()