  import os
  def get_current_directory():
        return os.getcwd()
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a