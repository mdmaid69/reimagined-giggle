  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import datetime
def get_current_date():
        return datetime.date.today()