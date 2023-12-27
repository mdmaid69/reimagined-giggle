  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))