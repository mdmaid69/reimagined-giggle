  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a