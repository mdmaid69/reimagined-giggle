  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))