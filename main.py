import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)