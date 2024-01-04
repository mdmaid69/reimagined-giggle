  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a