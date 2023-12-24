  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))