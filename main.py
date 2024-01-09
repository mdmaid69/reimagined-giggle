  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a