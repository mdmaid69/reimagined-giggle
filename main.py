  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))