  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))