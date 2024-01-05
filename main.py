  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import datetime
def get_current_date():
        return datetime.date.today()