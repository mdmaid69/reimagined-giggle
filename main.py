  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def calculate_area(radius):
        return 3.14 * radius * radius