import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()