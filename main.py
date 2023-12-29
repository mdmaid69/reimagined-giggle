  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))