sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)