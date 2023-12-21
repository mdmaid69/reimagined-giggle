import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)