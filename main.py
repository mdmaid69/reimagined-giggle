sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)