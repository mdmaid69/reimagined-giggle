import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)