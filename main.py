  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()