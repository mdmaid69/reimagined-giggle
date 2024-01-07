  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))