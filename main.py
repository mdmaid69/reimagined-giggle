  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))