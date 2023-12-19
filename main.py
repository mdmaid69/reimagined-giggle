import datetime
def get_today_date():
        return datetime.date.today()
  import os
  def get_base_name(path):
        return os.path.basename(path)