  import os
  def get_current_working_directory():
        return os.getcwd()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())