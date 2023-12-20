import array
def iterate_over_array(array):
        for item in array:
        print(item)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]