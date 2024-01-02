  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
def calculate_area(radius):
        return 3.14 * radius * radius