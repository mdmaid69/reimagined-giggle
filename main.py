sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink