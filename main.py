  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import shutil
def delete_directory(path):
        shutil.rmtree(path)