  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a