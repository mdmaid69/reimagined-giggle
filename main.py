  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)