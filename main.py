import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)