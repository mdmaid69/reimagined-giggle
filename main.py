import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)