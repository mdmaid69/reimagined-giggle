import datetime
print(datetime.datetime.now())
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)