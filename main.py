import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import os
  def delete_file(file_name):
        os.remove(file_name)