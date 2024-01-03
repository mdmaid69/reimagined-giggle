  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))