  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))