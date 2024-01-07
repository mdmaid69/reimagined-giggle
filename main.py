import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)