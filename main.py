import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns