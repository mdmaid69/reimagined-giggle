import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]