sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def get_directory_name(path):
        return os.path.dirname(path)