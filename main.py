  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))