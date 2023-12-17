  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a