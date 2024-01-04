  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))