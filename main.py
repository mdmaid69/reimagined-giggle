import datetime
def get_current_date():
        return datetime.date.today()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)