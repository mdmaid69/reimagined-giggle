  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))