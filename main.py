  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))