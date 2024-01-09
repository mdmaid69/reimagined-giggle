  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))