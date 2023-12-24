  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))