  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
i = 0
while i < 5:
        print(i)
        i += 1