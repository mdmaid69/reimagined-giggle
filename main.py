import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()