  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))