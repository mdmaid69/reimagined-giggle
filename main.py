import datetime
def get_current_date():
        return datetime.date.today()
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)