import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()