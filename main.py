  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a