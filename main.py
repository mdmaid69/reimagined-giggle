  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()