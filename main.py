  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
text = "Hello, world!"
print("Characters:", len(text))