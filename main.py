  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a