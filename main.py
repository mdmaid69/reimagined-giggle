import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)