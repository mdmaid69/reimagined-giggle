  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a