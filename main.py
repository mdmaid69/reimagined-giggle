  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))