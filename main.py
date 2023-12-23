  import os
  def delete_file(file_name):
        os.remove(file_name)
import datetime
def get_current_date():
        return datetime.date.today()