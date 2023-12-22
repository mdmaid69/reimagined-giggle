  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import glob
def find_files(pattern):
        return glob.glob(pattern)