import datetime
print(datetime.datetime.now())
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)