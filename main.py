  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a