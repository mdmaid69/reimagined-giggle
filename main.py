  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
n = 10
print("Cube numbers:", [x**3 for x in range(n)])