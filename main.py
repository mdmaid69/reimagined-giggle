import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)