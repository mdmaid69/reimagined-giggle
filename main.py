  import os
  def split_path(path):
        return os.path.split(path)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))