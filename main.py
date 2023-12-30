  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import datetime
print(datetime.datetime.now())