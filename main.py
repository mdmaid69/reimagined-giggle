  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))