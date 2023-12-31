import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)