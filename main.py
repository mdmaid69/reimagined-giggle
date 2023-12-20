  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a