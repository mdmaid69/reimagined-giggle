  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
print([x**2 for x in range(10)])