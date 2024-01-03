import datetime
print(datetime.datetime.now())
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)