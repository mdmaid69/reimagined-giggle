  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a