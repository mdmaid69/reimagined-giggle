sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)