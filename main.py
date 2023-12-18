  import os
  def get_base_name(path):
        return os.path.basename(path)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)