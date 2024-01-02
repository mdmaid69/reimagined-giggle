  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))